import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper, Grid, Card, CardContent } from '@mui/material';
import api from '../services/api';

export default function Risk() {
  const [behaviors, setBehaviors] = useState<any[]>([]);

  useEffect(() => {
    fetchRisk();
  }, []);

  const fetchRisk = async () => {
    try {
      const res = await api.get('/risk/behavior/');
      setBehaviors(res.data.results);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Risk Analysis</Typography>
      <Grid container spacing={3}>
        {behaviors?.map((b) => (
          <Grid size={{ xs: 12, md: 4 }} key={b.id}>
            <Card sx={{ bgcolor: b.risk_level === 'CRITICAL' ? 'error.main' : b.risk_level === 'HIGH' ? 'warning.main' : 'background.paper' }}>
              <CardContent>
                <Typography variant="h6">User ID: {b.user}</Typography>
                <Typography>Risk Level: {b.risk_level}</Typography>
                <Typography>Risk Score: {b.risk_score}</Typography>
                <Typography>Failed Logins: {b.failed_login_count}</Typography>
                <Typography>Activity Freq: {b.activity_frequency.toFixed(2)}</Typography>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>
    </Box>
  );
}
