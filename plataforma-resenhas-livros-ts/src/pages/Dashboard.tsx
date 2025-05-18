import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { jwtDecode, JwtPayload } from "jwt-decode";

const Dashboard: React.FC = () => {
  const navigate = useNavigate();
  const [token, setToken] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const savedToken = localStorage.getItem("jwt_token");

    if (!savedToken) {
      console.warn("🔐 Token ausente. Redirecionando para /login");
      navigate("/login");
      return;
    }

    try {
      const decoded = jwtDecode<JwtPayload>(savedToken);

      if (!decoded.exp || decoded.exp < Date.now() / 1000) {
        console.warn("⏰ Token expirado ou sem exp. Redirecionando para /login");
        localStorage.removeItem("jwt_token");
        navigate("/login");
        return;
      }

      setToken(savedToken);
    } catch (err) {
      console.error("❌ Token inválido:", err);
      localStorage.removeItem("jwt_token");
      navigate("/login");
    } finally {
      setLoading(false);
    }
  }, [navigate]);

  if (loading) return <p>Validando sessão...</p>;

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Bem-vindo ao Dashboard</h1>
      <p><strong>Token JWT:</strong></p>
      <code style={{ wordBreak: "break-all" }}>{token}</code>
    </div>
  );
};

export default Dashboard;