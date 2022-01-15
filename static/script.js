const filtermenu = () => {
  $(".shadow-screen").removeClass("d-none");
  $(".filter-box").animate(
    {
      visibility: "visible",
      height: "300px",
      width: "250px",
      borderRadius: "16px",
    },
    1000
  );
};

const removeShadow = () => {
  $(".shadow-screen").addClass("d-none");
  $(".filter-box").animate(
    { visibility: "hidden", height: 0, width: 0, borderRadius: "30px" },
    500
  );
};
