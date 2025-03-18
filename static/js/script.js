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

  