let TOKEN ='7597406786:AAHk4DubZT96zxY_Qm1s0FzH64evyaX6xK8';
let CHAT_ID= -1002392730094;
let URL_API = `https://api.telegram.org/bot${ TOKEN}/sendMessage`;


document.getElementById('tg').addEventListener('submit', function(e) {
  e.preventDefault();

  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  let message = `<b>Ro'yxat Balita</b>\n`;
  message += `<b>Ism:</b> ${this.name.value}\n`;
  message += `<b>Raqam:</b> ${this.number.value}\n`;
  message += `<b>Email:</b> ${this.email.value}\n`;
  message += `<b>Xabar:</b> ${this.message.value}`;

  console.log(message);

  axios.post(URL_API, {
      chat_id: CHAT_ID,
      parse_mode: 'html',
      text: message
  }, {
      headers: {
          'X-CSRFToken': csrfToken  
      }
  })
  .then((response) => {
      console.log('Success:', response.data);
      this.name.value = '';
      this.number.value = '';
      this.email.value = '';
      this.message.value = '';
  })
  .catch((error) => {
      console.error('Error:', error);
  })
  .finally(() => {
      console.log('Request finished');
  });
});

