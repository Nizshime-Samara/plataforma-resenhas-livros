import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const navigate = useNavigate();
  const [token, setToken] = useState(null);

  useEffect(() => {
    const savedToken = localStorage.getItem("jwt_token");
    if (!savedToken) {
      navigate("/login");
    } else {
      setToken(savedToken);
    }
  }, [navigate]);

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Bem-vindo ao Dashboard - Login</h1>
      <p><strong>Token JWT:</strong></p>
      <code>{token}</code>
    </div>
  );
};

export default Dashboard;
