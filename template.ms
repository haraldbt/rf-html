<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>RF Meny</title>
    <style>
      html {
        font-family: arial, sans-serif;
      }
      .prod {
        width: 40%;
      }
      .size {
        width: 12%;
      }
      .abv {
        width: 12%;
      }
      .orig {
        width: 25%;
      }

      .price {
        width: 11%;
      }

      table {
        border-collapse: collapse;
        width: 100%;
      }

      td,
      th {
        border: 1px solid #dddddd;
        text-align: left;
        padding: 8px;
      }

      tr:nth-child(even) {
        background-color: #dddddd;
      }
    </style>
  </head>
  <body>
    {{#categories}}
    <h1>{{name}}</h1>
    <table>
      <thead>
        <tr>
          <th>Produkt</th>
          <th>Størrelse</th>
          <th>ABV</th>
          <th>Land/sted</th>
          <th>Pris</th>
        </tr>
      </thead>
      <tbody>
        {{#products}}
        <tr>
          <td class="prod">{{name}}</td>
          <td class="size">{{size}}</td>
          <td class="abv">{{abv}}</td>
          <td class="orig">{{country}}</td>
          <td class="price">{{price}}</td>
        </tr>
        {{/products}}
      </tbody>
    </table>
    {{/categories}}
  </body>
</html>
