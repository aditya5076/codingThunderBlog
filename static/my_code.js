document.addEventListener('DOMContentLoaded', function (event) {
  console.log('hello fellas');
  let sc = document.createElement('script');
  sc.setAttribute(
    'src',
    'https://cdnjs.cloudflare.com/ajax/libs/tinymce/4.5.12/tinymce.min.js'
  );

  document.head.appendChild(sc);
  sc.onload = () => {
    tinymce.init({ selector: '#id_content' });
  };
});
