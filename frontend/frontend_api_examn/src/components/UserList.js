import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './styles.css'; // Importa tu archivo CSS

function UserList() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Realizar la solicitud GET a tu API aquí
    axios.get('http://127.0.0.1:5000/califications')
      .then((response) => {
        setData(response.data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Cargando...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <header>
        <h1>EXÁMEN FINAL Desarrollo de Aplicaciones Web-NRC 10522</h1>
      </header>
      <table>
        <thead>
          <tr>
            <th>Nombre</th>
            <th>Descripción</th>
            <th>Unidad</th>
            <th>Calificación</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item) => (
            <tr key={item._id}>
              <td>{item.Name}</td>
              <td>{item.Description}</td>
              <td>{item.Unit}</td>
              <td>{item.Grade}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <footer>
        <p>Creado por ⚓ Estudiantes de la Universidad de las Fuerzas Armadas ESPE</p>
      </footer>
    </div>
  );
}

export default UserList;
