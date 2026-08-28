import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Chip } from '@mui/material';
import api from '../services/api';
import type { Incident } from '../types';

export default function Incidents() {
  const [incidents, setIncidents] = useState<Incident[]>([]);

  useEffect(() => {
    api.get('/incidents/').then(res => setIncidents(res.data.results)).catch(console.error);
  }, []);

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Incident Management</Typography>
      <Paper sx={{ width: '100%', overflow: 'hidden' }}>
        <TableContainer sx={{ maxHeight: 600 }}>
          <Table stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell>Title</TableCell>
                <TableCell>Severity</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Assigned To</TableCell>
                <TableCell>Created At</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {incidents.map((row) => (
                <TableRow hover key={row.id}>
                  <TableCell>{row.title}</TableCell>
                  <TableCell><Chip label={row.severity} size="small" /></TableCell>
                  <TableCell>{row.status}</TableCell>
                  <TableCell>{row.assigned_to_name || 'Unassigned'}</TableCell>
                  <TableCell>{new Date(row.created_at).toLocaleString()}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
    </Box>
  );
}
