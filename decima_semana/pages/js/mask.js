function phoneMask(context) {
  phone = context.value;

  phone = phone.replace(/\D/g, "");
  phone = phone.replace(/^(\d{2})(\d)/g, "($1) $2");
  phone = phone.replace(/(\d)(\d{3})$/, "$1-$2");

  context.value = phone;
}

function idMask(context) {
  id = context.value;

  id = id.replace(/\D/g, "")
  id = id.replace(/(\d{3})(\d)/, "$1.$2")
  id = id.replace(/(\d{3})(\d)/, "$1.$2")
  id = id.replace(/(\d{3})(\d{1,2})$/, "$1-$2")

  context.value = id;
}