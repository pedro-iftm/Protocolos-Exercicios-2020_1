function phoneMask(context) {
  phone = context.value;

  phone = phone.replace(/\D/g, "");
  phone = phone.replace(/^(\d{2})(\d)/g, "($1) $2");
  phone = phone.replace(/(\d)(\d{3})$/, "$1-$2");

  context.value = phone;
}

function idMask(context) {
  id = context.value;

  id = id.replace(/\D/g, "");
  id = id.replace(/(\d{3})(\d)/, "$1.$2");
  id = id.replace(/(\d{3})(\d)/, "$1.$2");
  id = id.replace(/(\d{3})(\d{1,2})$/, "$1-$2");

  context.value = id;
}

function renderMessage(message) {
  document.getElementById('message').innerHTML = message
}

function validateNumericField(fieldName, value, length) {
  formatedValue = value.replace(/[^a-z0-9]/gi, '');

  if (isNaN(formatedValue)) {
    renderMessage(fieldName + ' permite somente números');
    return false;
  }

  if (value.length !== length) {
    renderMessage(fieldName + ' muito curto');
    return false;
  }
  return true;
}

function getValue(fieldName) {
  return document.forms['add-contact'][fieldName].value;
}

function validateName(name) {
  regexSpecialCharacters = /[^a-z0-9]/gi;
  regexNumber = /\d/;

  if (regexSpecialCharacters.test(name) || regexNumber.test(name)) {
    message = /\d/.test(name)
      ? 'Não são permitidos números no nome'
      : 'Não são permitidos caracteres especiais no nome';
    renderMessage(message);
    return false;
  }

  return true;
}

function validateForm() {

  id = getValue('id');
  phone = getValue('phone');
  email = getValue('email');
  name = getValue('name');
  console.log([id, phone, email, name]);

  if (![id, phone, email, name].every(element => element)) {
    renderMessage('Preencha todos os campos')
    return false;
  }

  if (!validateName(name)
    || !validateNumericField('CNPJ', id, 14)
    || !validateNumericField('Telefone', phone, 15)) {
    return false;
  }

  return true
}