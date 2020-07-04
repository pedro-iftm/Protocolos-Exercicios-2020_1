<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="styles/list.css">
  <title>List Contacts</title>
</head>

<body>
  <div class="card center-card">
    <button>
      <a href="/add-contact">NOVO</a>
    </button>
    <form action="/search-contacts" method="GET">
      <input type="text" placeholder="Pesquisar" name="search">
      <input type="submit" name="search_button" value="PESQUISAR">
    </form>
    <hr>
    <form action="/sort-contacts" method="GET">
      <table>
        <tr>
          <th><input class="header" type="submit" name="sort_name" value="NOME"></th>
          <th><input class="header" type="submit" name="sort_id" value="CPF"></th>
          <th><input class="header" type="submit" name="sort_email" value="EMAIL"></th>
          <th><input class="header" type="submit" name="sort_phone" value="TELEFONE"></th>
          <th></th>
          <th></th>
        </tr>
        % if rows:
          % for row in rows:
            <tr>
              % for col in row:
                <td>{{ col }}</td>
              % end
              <td>
                <button>
                  <a href="edit-contact?id={{ row[1] }}">Editar</a>
                </button>
              </td>
              <td>
                <button>
                  <a href="delete-contact?id={{ row[1] }}">Excluir</a>
                </button>
              </td>
            </tr>
          % end
        % end
      </table>
    </form>
  </div>
</body>

</html>