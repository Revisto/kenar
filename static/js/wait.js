// Vars

function Room(fill, viewBox, items) {
	this.value = 0;
	this.items = items || 4;
	this.fill = fill;
	this.viewBox = viewBox;
}

var rooms = {
	dressingroom: new Room('#cd5c5c', '30 202 150 100', 3),
	livingroom: new Room('#66cdaa', '153 198 165 105'),
	kitchen: new Room('#f0e68c', '305 202 150 100'),
	bedroom: new Room('#ffe4c4', '103 104 155 98'),
	bathroom: new Room('#ffffe0', '259 104 165 100', 3),
	cabinet: new Room('#d8Bfd8', '105 -20 255 150', 3),
	totalItems: 0
}

var tlThrowItems = new TimelineMax();
var tlEnd = new TimelineMax({paused: true});

// Set

TweenMax.set(['.item', '.place', '#ground', '#smile'], {
	transformOrigin: 'center'
})
TweenMax.set('.item', {
	autoAlpha: 1
})

// Timelines

tlThrowItems
	.staggerFrom('.item', .35, {
		y: 300,
		ease: Elastic.easeOut.config(.3)
	}, .1);

tlEnd
	.to('#ground', .55, {
		morphSVG: '#smile',
		delay: 1.05
	});

// Draggable

var s = 4;

Draggable.create('.item', {
	bounds: window,
	throwProps: true,
	snap: {
		x: function(endValue) {
			return Math.round(endValue / s) * s;
		},
		y: function(endValue) {
			return Math.round((endValue) / s) * s;
		}
	},
	onDrag: onDrag,
	onDragEnd: onDragEnd
});

function onDragEnd() {
	cursorShow();
	zoomOut();
	
	var hitTarget = this.target.getAttribute('data-item');
	var room = this.target.getAttribute('data-room');
	var dirty = +this.target.getAttribute('data-dirty');

	if (this.hitTest('#' + room, '70 %') && !dirty) {
		rooms[room].value++;
		rooms.totalItems++;
		this.target.setAttribute('data-dirty', 1);
	}	else if (!this.hitTest('#' + room, '70 %') && dirty) {
		rooms[room].value--;
		rooms.totalItems--;
		this.target.setAttribute('data-dirty', 0);
	}
	
	if (rooms[room].value >= rooms[room].items) {
		TweenMax.to('#' + room, .85, {
			fill: rooms[room].fill,
			ease: Back.easeOut
		})
	}
	
	if (rooms.totalItems >= 21) {
		tlEnd.play();
	}
}

function onDrag() {
	
	var hitTarget = this.target.getAttribute('data-item');
	var room = this.target.getAttribute('data-room');

	if (this.hitTest('#' + room, '85 %')) {
		TweenMax.to('.item-' + hitTarget, .6, {
			scale: 1.05,
			ease: Bounce.easeOut
		})
		TweenMax.to('.place-' + hitTarget, .35, {
			scale: 0
		})
	} else {
		TweenMax.to('.item-' + hitTarget, .4, {
			scale: 1,
			ease: Bounce.easeOut
		})
		TweenMax.to('.place-' + hitTarget, .3, {
			scale: 1
		})
	}
	
	if (this.hitTest('#' + room, '50%')) {
		cursorHide();
		zoomIn(rooms[room].viewBox);
	} else {
		cursorShow();
		zoomOut();
	}
}

// Helpers

function cursorHide() {
	TweenMax.set('svg', {
		className: 'no-cursor',
	})
}
function cursorShow() {
	TweenMax.set('svg', {
		className: ''
	})
}

function zoomIn(viewBox) {
	TweenMax.to('svg', .95, {
		attr: {
			viewBox: viewBox
		},
		ease: Power3.easeOut
	})
}

function zoomOut() {
	TweenMax.to('svg', 1.15, {
		attr: {
			viewBox: '0 0 500 500'
		},
		ease: Power3.easeOut
	})
}