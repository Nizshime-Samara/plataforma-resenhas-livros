import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const navigate = useNavigate();
  const [token, setToken] = useState(null)

  useEffect(() => {
    const savedToken = localStorage.getItem("jwt_token");

    if (!savedToken) {
      console.warn("🔐 Token ausente. Redirecionando para /login");
      navigate("/login");
    } else {
      setToken(savedToken);
    }
  }, [navigate]);

  if (!token) {
    return <p>Carregando painel...</p>; 
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Bem-vindo ao Dashboard</h1>
      <p><strong>Token JWT:</strong></p>
      <code style={{ wordBreak: "break-all" }}>{token}</code>
    </div>
  );
};

export default Dashboard;
