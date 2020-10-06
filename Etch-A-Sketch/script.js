var size = 16;

$(document).ready(function() {
  makeGrid();
  $(".button").click(function() {
    $('div').removeClass("active");
    size = prompt("Please insert grip size");
    if (size > 64) {size = 64};
    reset();
  });
});

function makeGrid() {
  for (i=1;i<=size*size;i++) {
    $(".container").append("<div class='grid'></div>");
  };
  $(".container").width(320 + "px");
  $(".container").height(320 + "px");
  $(".grid").width(320/(size));
  $(".grid").height(320/(size));
};

function reset() {
  $(".container").empty();
  makeGrid();
};

$(document).on("mouseenter", ".grid", function() {
  $(this).addClass("active");
});