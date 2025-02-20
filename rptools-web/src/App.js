import { BrowserRouter as Router, Routes, Route, Link, useNavigate } from 'react-router-dom';
import { useState } from 'react';

function App() {
  return (
    <Router>
      <div>
        {/* Навигация */}
        <nav>
          <Link to="/">DnD Web</Link> |
          <Link to="/register">Регистрация</Link> |
          <Link to="/profile">Личный кабинет</Link> |
          <Link to="/lobby">Лобби</Link>
        </nav>
        
        {/* Контент */}
        <Routes>
          <Route path="/" element={<WelcomePage />} />
          <Route path="/register" element={<RegisterPage />} />
          <Route path="/welcome" element={<WelcomeAfterRegister />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/lobby" element={<LobbyPage />} />
          <Route path="/table/:lobbyId" element={<TablePage />} />
        </Routes>
      </div>
    </Router>
  );
}

function WelcomePage() {
  return <div><h1>DnD Web</h1><p>BEST WEB SITE EVER!!!</p></div>;
}

function RegisterPage() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Регистрация:', { username, email, password });
    navigate('/welcome');
  };

  return (
    <div>
      <h1>Регистрация</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Имя пользователя" value={username} onChange={(e) => setUsername(e.target.value)} required /><br />
        <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} required /><br />
        <input type="password" placeholder="Пароль" value={password} onChange={(e) => setPassword(e.target.value)} required /><br />
        <button type="submit">Зарегистрироваться</button>
      </form>
    </div>
  );
}

function WelcomeAfterRegister() {
  return <div><h1>Спасибо за регистрацию!</h1></div>;
}

function ProfilePage() {
  return <div><h1>Личный кабинет</h1></div>;
}

function LobbyPage() {
  return <div><h1>Лобби</h1><p>background_image_lobby_page.png</p></div>;
}

function TablePage() {
  return <div><h1>Игровой стол</h1><p>background_image_table_page.png</p></div>;
}

export default App;
