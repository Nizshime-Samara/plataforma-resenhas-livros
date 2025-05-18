import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const AuthCallback: React.FC = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const searchParams = new URLSearchParams(window.location.search);
    const hashParams   = new URLSearchParams(window.location.hash.slice(1)); // remove '#'
    const token = searchParams.get("token") || hashParams.get("token");

    if (token) {
      localStorage.setItem("jwt_token", token);
      navigate("/dashboard");
    } else {
      console.warn("❌ Token não encontrado no callback.");
      navigate("/login");
    }
  }, [navigate]);

  return <p>Autenticando...</p>;
};

export default AuthCallback;
