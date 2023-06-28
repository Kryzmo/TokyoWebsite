$(window).scroll(function () {
	if ($(window).scrollTop() == $(document).height() - $(window).height()) {
	}
});
$(document).ready(function () {
	let prevScrollpos = window.pageYOffset;

	window.onscroll = function () {
		let currentScrollPos = window.pageYOffset;
		if (currentScrollPos < prevScrollpos - 10) {
			document.getElementById("mobile-bar").style.bottom = "-1px";
		} else if (currentScrollPos > prevScrollpos + 10) {
			document.getElementById("mobile-bar").style.bottom = "-140px";
		}
		prevScrollpos = currentScrollPos;
	};
});
