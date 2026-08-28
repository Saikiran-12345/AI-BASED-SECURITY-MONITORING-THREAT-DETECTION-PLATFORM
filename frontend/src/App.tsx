import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';

// Pages
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Events from './pages/Events';
import Alerts from './pages/Alerts';
import Risk from './pages/Risk';
import Incidents from './pages/Incidents';
import MainLayout from './layouts/MainLayout';

const darkTheme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#90caf9',
    },
    secondary: {
      main: '#f48fb1',
    },
    background: {
      default: '#0a1929',
      paper: '#001e3c',
    },
  },
});

const PrivateRoute = ({ children }: { children: React.ReactElement }) => {
  const isAuthenticated = !!localStorage.getItem('token');
  return isAuthenticated ? children : <Navigate to="/login" />;
};

function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/login" element={<Login />} />
          
          <Route path="/" element={<PrivateRoute><MainLayout /></PrivateRoute>}>
            <Route index element={<Dashboard />} />
            <Route path="events" element={<Events />} />
            <Route path="alerts" element={<Alerts />} />
            <Route path="risk" element={<Risk />} />
            <Route path="incidents" element={<Incidents />} />
          </Route>
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;

