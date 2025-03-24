console.log([
    {% for availability in availabilities %}
    {
      title: 'Available',
      start: '{{ availability.start_time|date:"Y-m-d\TH:i:s" }}',
      end: '{{ availability.end_time|date:"Y-m-d\TH:i:s" }}',
      color: '#28a745'
    },
    {% endfor %}
  ]);


document.addEventListener("DOMContentLoaded", function () {
        const scrollingContainer = document.querySelector(".scrolling-container");

        let scrollAmount = 0;

        function autoScroll() {
            scrollAmount += 1; // Adjust the scroll speed here
            scrollingContainer.scrollLeft = scrollAmount;

            // Reset scroll position to create a seamless loop
            if (scrollAmount >= scrollingContainer.scrollWidth / 2) {
                scrollAmount = 0;
            }

            requestAnimationFrame(autoScroll);
        }

        autoScroll();
    });


  