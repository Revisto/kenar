from flask import Blueprint, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import os
import requests

from db import post_operations
from services.meshy_service import MeshyService
from services.image_uploader_service import ImageUploader
from config import Config

main = Blueprint('main', __name__)

@main.route('/<post_id>/view')
def view(post_id):
    post = post_operations.get_post_by_id(post_id)
    if post:
        if post.model_status == 'COMPLETED':
            pass
        elif post.model_status == 'FAILED':
            flash('Model creation failed')
            return render_template('error.html')
        else:
            task_id = post.task_id
            meshy_service = MeshyService(Config.MESHY_API_KEY)
            task = meshy_service.retrieve_image_to_3d_task(task_id)
            if task['status'] == 'SUCCEEDED':
                model_file_url = task['model_urls']["glb"]
                model_file = os.path.join("static", f"{post_id}.glb")
                with open(model_file, 'wb') as file:
                    response = requests.get(model_file_url)
                    file.write(response.content)
                post_operations.update_post_status(post_id, 'SUCCEEDED')
            elif task['status'] == 'FAILED' or task['status'] == 'EXPIRED':
                flash('Model creation failed')
                post_operations.update_post_status(post_id, task["status"])
                return render_template('error.html', error=task['error'])
            elif task['status'] == 'IN_PROGRESS' or task['status'] == 'PENDING':
                flash('Model creation in progress')
                return render_template('wait.html', progress=task['progress'])
            else:
                flash('Unknown status')
                return render_template('error.html', error='Unknown status')
    else:
        flash('Post not found')
        return render_template('error.html', error='Post not found')
    
    model_file = url_for('static', filename=f"{post_id}.glb")
    return render_template('view.html', model_file=model_file)

@main.route('/<post_id>/upload', methods=['GET'])
def upload(post_id):
    # check if the post exists in the database
    post = post_operations.get_post_by_id(post_id)
    if post:
        flash('Post already exists')
        return render_template('success.html', view_url=url_for('main.view', post_id=post_id))
    return render_template('upload.html')

@main.route('/<post_id>/upload', methods=['POST'])
def upload_post(post_id):
    # check if the post exists in the database
    post = post_operations.get_post_by_id(post_id)
    if post:
        flash('Post already exists')
        return render_template('success.html', view_url=url_for('main.view', post_id=post_id))
    
    if 'file' in request.files and request.files['file'].filename != '':
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file_format = file.filename.split('.')[-1]
            if file_format not in Config.ALLOWED_EXTENSIONS:
                flash('Invalid file format')
                return redirect(request.url)
            filename = f"{post_id}.{file_format}"
            file.save(os.path.join("./", filename))
            task_id = MeshyService(Config.MESHY_API_KEY).create_image_to_3d_task(ImageUploader(Config.IMAGE_UPLOAD_URL).upload_image_from_file(filename))
            os.remove(filename)
            post_operations.create_new_post(post_id, task_id)
            flash('File successfully uploaded')
            view_url = url_for('main.view', post_id=post_id)
            return render_template('success.html', view_url=view_url)
    elif 'url' in request.form and request.form['url'] != '':
        image_url = request.form['url']
        task_id = MeshyService(Config.MESHY_API_KEY).create_image_to_3d_task(image_url)
        post_operations.create_new_post(post_id, task_id)
        flash('URL received')
        view_url = url_for('main.view', post_id=post_id)
        return render_template('success.html', view_url=view_url)
    else:
        flash('No file or URL provided')
        return redirect(request.url)
    
# handle upload/?post_token=gZFmMQKr and redicrext to /<post_id>/upload
@main.route('/upload', methods=['GET'])
def upload_redirect():
    post_id = request.args.get('post_token')
    return redirect(url_for('main.upload', post_id=post_id))

@main.route('/')
def test_success_page():
    return render_template('wait2.html')