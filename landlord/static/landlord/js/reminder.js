var today = new Date()

var moveInCalendar = app.calendar.create({
    inputEl: '#id_next_service',
    openIn: 'customModal',
    header: true,
    footer: true,
    dateFormat: 'yyyy-mm-dd',
    disabled: function (date) {
        if (date.getFullYear() < today.getFullYear() || date.getDate() < today.getDate()) {
            return true;
        }
        else {
            return false;
        }
    },
});
