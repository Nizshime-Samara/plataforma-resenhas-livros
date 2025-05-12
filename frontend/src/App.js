import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Login from './pages/Login';
import AuthCallback from './pages/AuthCallback';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/auth/callback" element={<AuthCallback />} />        
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />        
        <Route path="*" element={<p>Página não encontrada</p>} />
      </Routes>
    </Router>
  );
}

export default App;