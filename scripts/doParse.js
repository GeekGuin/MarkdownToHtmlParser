marked.setOptions({
	renderer: new marked.Renderer(),
	gfm: true,
	tables: true,
	breaks: false,
	pedantic: false,
	sanitize: false,
	smartLists: true,
	smartypants: false,
	emoji: function (emoji) {
    	return '<img src="'
			+ 'graphics/emojis/'
			+ encodeURIComponent(emoji)
			+ '.png"'
			+ ' alt=":'
			+ escape(emoji)
			+ ':"'
			+ ' title=":'
			+ escape(emoji)
			+ ':"'
			+ ' class="emoji" align="absmiddle" height="20" width="20">';
  	}
});

var renderer = new marked.Renderer();

renderer.heading = function (text, level) {
  	var escapedText = text.toLowerCase().replace(/[^\w]+/g, '-');

	return '<h' + level + '><a name="' +
	            escapedText +
	             '" class="anchor" href="#' +
	             escapedText +
	             '"><span class="header-link"></span></a>' +
	              text + '</h' + level + '>';
}

var update = function(){
	document.getElementById('content').innerHTML = marked(document.getElementById('input').value, { renderer: renderer });
}

update();
