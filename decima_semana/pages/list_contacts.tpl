<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles/common.css">
  <link rel="stylesheet" href="styles/list_contacts.css">
  <title>List Contacts</title>
</head>

<body>
  <div class="card center-card">
    <button>
      <a href="/">VOLTAR</a>
    </button>
    <hr>
    <table>
      <tr>
        <th>NOME</th>
        <th>CPF</th>
        <th>EMAIL</th>
        <th>TELEFONE</th>
      </tr>
      % if rows:
        % for row in rows:
        <tr>
          % for col in row:
            <td>{{ col }}</th>
          % end
        </tr>
        % end
      % end
    </table>
  </div>
</body>

</html>