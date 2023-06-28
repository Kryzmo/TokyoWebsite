var owl = $(".owl-carousel");
owl.owlCarousel({
	lazyLoad: true,
	// autoplay: true,
	autoplayTimeout: 3000,
	autoplayHoverPause: true,
	loop: true,
	margin: 0,
	center: true,
	responsive: {
		0: {
			items: 1,
		},
	},
});
// owl.on("mousewheel", ".owl-stage", function (e) {
// 	if (e.deltaY > 0) {
// 		owl.trigger("prev.owl");
// 	} else {
// 		owl.trigger("next.owl");
// 	}
// 	e.preventDefault();
// });

$(".owl-prev").click(function () {
	$(".owl-carousel").trigger("prev.owl.carousel");
});

$(".owl-next").click(function () {
	$(".owl-carousel").trigger("next.owl.carousel");
});
