import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import AuthCallBack from './pages/AuthCallBack';


const App: React.FC = () => (
  <BrowserRouter>
    <Routes>
      {/* redireciona “/” → “/login” */}
      <Route path="/" element={<Navigate to="/login" replace />} />

      <Route path="/login" element={<Login />} />
      <Route path="/auth/callback" element={<AuthCallBack />} />
      <Route path="/dashboard" element={<Dashboard />} />

      {/* rota coringa para 404 simples */}
      <Route path="*" element={<p>Página não encontrada</p>} />
    </Routes>
  </BrowserRouter>
);

