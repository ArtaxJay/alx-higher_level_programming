$('document').ready(() => {
  $('INPUT#btn_translate').click(translateFunc);
  $('INPUT#language_code').focus(() => {
    $(this).keydown(e => {
      if (e.keyCode === 13) {
        translateFunc();
      }
    });
  });
});

function translateFunc () {
  const langUrl = 'https://www.fourtonfish.com/hellosalut/?';
  $.get(langUrl + $.param({ lang: $('INPUT#language_code').val() }), res =>
    $('DIV#hello').html(res.hello)
  );
}
