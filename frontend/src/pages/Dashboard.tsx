import React, { useEffect, useState } from 'react';
import { Grid, Paper, Typography, Box, CircularProgress, Card, CardContent } from '@mui/material';
import api from '../services/api';
import type { DashboardStats } from '../types';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

export default function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const res = await api.get('/analytics/dashboard-stats/');
        setStats(res.data);
      } catch (err) {
        console.error(err);
      } finally {
        setLoading(false);
      }
    };
    fetchStats();
  }, []);

  if (loading) return <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}><CircularProgress /></Box>;

  const mockChartData = [
    { name: 'Mon', events: 400 },
    { name: 'Tue', events: 300 },
    { name: 'Wed', events: 550 },
    { name: 'Thu', events: 200 },
    { name: 'Fri', events: 278 },
    { name: 'Sat', events: 189 },
    { name: 'Sun', events: 239 },
  ];

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Security Dashboard</Typography>
      
      <Grid container spacing={3} sx={{ mb: 4 }}>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ bgcolor: 'info.dark' }}>
            <CardContent>
              <Typography color="textSecondary" gutterBottom>Total Events</Typography>
              <Typography variant="h3">{stats?.total_events}</Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ bgcolor: 'warning.dark' }}>
            <CardContent>
              <Typography color="textSecondary" gutterBottom>Total Threats</Typography>
              <Typography variant="h3">{stats?.total_threats}</Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ bgcolor: 'error.dark' }}>
            <CardContent>
              <Typography color="textSecondary" gutterBottom>Total Alerts</Typography>
              <Typography variant="h3">{stats?.total_alerts}</Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid size={{ xs: 12, sm: 6, md: 3 }}>
          <Card sx={{ bgcolor: 'success.dark' }}>
            <CardContent>
              <Typography color="textSecondary" gutterBottom>Recent Events (7d)</Typography>
              <Typography variant="h3">{stats?.recent_events}</Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      <Grid container spacing={3}>
        <Grid size={{ xs: 12, md: 8 }}>
          <Paper sx={{ p: 2, height: 400 }}>
            <Typography variant="h6" gutterBottom>Events Overview</Typography>
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={mockChartData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="events" fill="#90caf9" />
              </BarChart>
            </ResponsiveContainer>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
}
