//Variables
let map;
let numeros = "0123456789";
let respuestas = {};
contenedor = document.getElementById("tabResultados");




//Funciones


function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 19.469921198890507, lng: -99.1221121217982 },
    zoom: 16,
  });
}

function fn_cp() {
  $("#exampleModal").modal("toggle");
  let cp = $("#cpPrin").val();
  if (tiene_numeros(cp) === 1) {

    $.ajax({
      type: "POST",
      url: "http://localhost:9500/busquedaCP",
      data: $("#formCpMapa").serialize(),
      processData: false,
      beforeSend: function () {},
      success: function (res) {
        respuestas = JSON.parse(res);
        console.log(respuestas);
        recorrerResultados(respuestas);
      },
      error: function (request, status, error) {
        console.log(request.responseText);
      },
    });
  } else {
    fn_estado();
    fn_colonia();
  }
}

function fn_estado() {
  $.ajax({
    type: "POST",
    url: "http://localhost:9500/busquedaEstado",
    data: $("#formCpMapa").serialize(),
    processData: false,
    beforeSend: function () {},
    success: function (res) {
      respuestas = JSON.parse(res);
      console.log(respuestas);
      recorrerResultados(respuestas);
    },
    error: function (request, status, error) {
      console.log(request.responseText);
    },
  });
}

function fn_colonia() {
  $.ajax({
    type: "POST",
    url: "http://localhost:9500/busquedaColonia",
    data: $("#formCpMapa").serialize(),
    processData: false,
    beforeSend: function () {},
    success: function (res) {
      respuestas = JSON.parse(res);
      console.log(respuestas);
      recorrerResultados(respuestas);
    },
    error: function (request, status, error) {
      console.log(request.responseText);
    },
  });
}

function tiene_numeros(texto) {
  for (i = 0; i < texto.length; i++) {
    if (numeros.indexOf(texto.charAt(i), 0) != -1) {
      return 1;
    }
  }
  return 0;
}

const recorrerResultados = (resultados) => {
  const result = resultados.map((dato) => {
    dibujarTabla(dato);
  });
};

const dibujarTabla = ({ tipo, lugar, municipio, estado }) => {
  contenedor = document.getElementById("tabResultados");
  const card = `
   <tr>
   <th>${tipo}</th>
   <th>${lugar}</th>
   <th>${municipio}</th>
   <th>${estado}</th>
   </tr>`;
  contenedor.insertAdjacentHTML("afterend", card);
};
