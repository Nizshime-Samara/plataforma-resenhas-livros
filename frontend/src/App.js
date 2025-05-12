import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import AuthCallback from './pages/AuthCallback';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <BrowserRouter basename="/plataforma-resenhas-livros">
      <Routes>
        <Route path="/" element={<Login />} /> {/* 👈 ADICIONADO */}
        <Route path="/login" element={<Login />} />
        <Route path="/auth/callback" element={<AuthCallback />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="*" element={<p>Página não encontrada</p>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;