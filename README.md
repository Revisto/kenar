
# Kenar Divar AR Furniture Viewer 🛋️👓

Welcome to the Kenar Divar AR Furniture Viewer! This innovative project was developed for the Kenar Divar Hackathon competition, aiming to revolutionize the way we interact with furniture listings online. By converting pictures of furniture from listings into 3D models (in GLB format) using AI, users can visualize these items in their actual size and place them in their homes using augmented reality (AR). This project leverages the power of AR to enhance the online shopping experience, making it more interactive and immersive.

![Kenar demo](https://raw.githubusercontent.com/Revisto/kenar/master/demo.jpg)

## Features 🌟

- **AR Visualization**: View furniture in your space with accurate dimensions using augmented reality.
- **3D Model Conversion**: Converts images from furniture listings into 3D models using the Meshy API.
- **Easy Upload**: Users can upload images or provide URLs for the furniture they wish to visualize.
- **Progress Tracking**: Monitor the status of the 3D model conversion process (pending, processing, completed).
- **Admin Mode**: Special access for admins to change scale of models to their exact needs.

![Kenar Divar](https://iranianstartup.com/wp-content/uploads/2024/01/%DA%A9%D9%86%D8%A7%D8%B1-1.png)

## Getting Started 🚀

### Prerequisites

- Python 3.6+
- Flask
- Flask-SQLAlchemy

### Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/revisto/kenar.git
   ```
2. Navigate to the project directory:
   ```sh
   cd kenar
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up the environment variables by copying the `.env.example` to `.env` and filling in your values.

### Running the Application

1. Start the Flask server:
   ```sh
   flask run
   ```
2. Open your web browser and navigate to `http://127.0.0.1:8000/` to start using the AR Furniture Viewer.

## Usage 📖

- **Viewing a Model**: Navigate to `/post_id/view` to view the AR model of a furniture item.
- **Uploading an Image**: Go to `/post_id/upload` to upload an image or provide an image URL for conversion.
- **Admin Access**: Add `?admin=true` to the view URL to access admin functionalities.

## Contributing 🤝

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📜

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements 💖

- [Meshy API](https://meshy.com) for 3D model conversion.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- All participants and organizers of the Kenar Divar Hackathon.

Let's bring the future of online furniture shopping to life! 🚀🏡
