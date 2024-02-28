$('DIV#toggle_header').click(() => {
  $('HEADER').toggleClass('green red');
  $('HEADER').removeClass(() =>
    $(this).hasClass('green') ? 'red' : 'green'
  );
});
