import React from "react";

const backendUrl = "https://plataforma-resenhas-livros.onrender.com";

const Login: React.FC = () => {
  const handleLogin = () => {
    window.location.href = `${backendUrl}/api/v1/auth/login/google`;
  };

  return (
    <div style={{ textAlign: "center", marginTop: "3rem" }}>
      <h1>Login</h1>
      <button onClick={handleLogin}>Entrar com Google</button>
    </div>
  );
};

export default Login;
