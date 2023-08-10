from . import create_app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)



#
#

#
#
# # <!-- In book_appointment.html -->
# # <select name="slot" id="slot">
# #     {% for slot in slots %}
# #         {% if is_slot_available(slot) %}
# #             <option value="{{ slot }}">{{ slot }}</option>
# #         {% else %}
# #             <option value="{{ slot }}" disabled>{{ slot }} - Booked</option>
# #         {% endif %}
# #     {% endfor %}
# # </select>
#
#

