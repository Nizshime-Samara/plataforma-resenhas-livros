import React from "react";

const Login = () => {
  const backendUrl = 'https://plataforma-resenhas-livros.onrender.com';

  const handleLogin = () => {
    const sessionId = crypto.randomUUID();

    localStorage.setItem("session_id", sessionId);

    window.location.href = `${backendUrl}/api/v1/auth/login/google?session_id=${sessionId}`;
  };

  return (
    <div style={{ textAlign: "center", marginTop: "3rem" }}>
      <h1>Login</h1>
      <button onClick={handleLogin}>Entrar com Google</button>
    </div>
  );
};

export default Login;