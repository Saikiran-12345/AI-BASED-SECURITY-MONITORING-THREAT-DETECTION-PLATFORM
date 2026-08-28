import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TablePagination, Chip } from '@mui/material';
import api from '../services/api';
import type { Alert } from '../types';
import { format } from 'date-fns';

export default function Alerts() {
  const [alerts, setAlerts] = useState<Alert[]>([]);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    fetchAlerts();
  }, [page, rowsPerPage]);

  const fetchAlerts = async () => {
    try {
      const res = await api.get(`/alerts/?page=${page + 1}&size=${rowsPerPage}`);
      setAlerts(res.data.results);
      setTotal(res.data.count);
    } catch (err) {
      console.error(err);
    }
  };

  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'CRITICAL': return 'error';
      case 'HIGH': return 'warning';
      case 'MEDIUM': return 'info';
      case 'LOW': return 'success';
      default: return 'default';
    }
  };

  return (
    <Box>
      <Typography variant="h4" gutterBottom>Active Alerts</Typography>
      <Paper sx={{ width: '100%', overflow: 'hidden' }}>
        <TableContainer sx={{ maxHeight: 600 }}>
          <Table stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell>Created At</TableCell>
                <TableCell>Message</TableCell>
                <TableCell>User</TableCell>
                <TableCell>Severity</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Risk Score</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {alerts.map((row) => (
                <TableRow hover key={row.id}>
                  <TableCell>{format(new Date(row.created_at), 'yyyy-MM-dd HH:mm:ss')}</TableCell>
                  <TableCell>{row.message}</TableCell>
                  <TableCell>{row.user_name || 'System'}</TableCell>
                  <TableCell>
                    <Chip label={row.severity} color={getSeverityColor(row.severity) as any} size="small" />
                  </TableCell>
                  <TableCell>{row.status}</TableCell>
                  <TableCell>{row.risk_score}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
        <TablePagination
          rowsPerPageOptions={[10, 25, 50]}
          component="div"
          count={total}
          rowsPerPage={rowsPerPage}
          page={page}
          onPageChange={(e, newPage) => setPage(newPage)}
          onRowsPerPageChange={(e) => {
            setRowsPerPage(parseInt(e.target.value, 10));
            setPage(0);
          }}
        />
      </Paper>
    </Box>
  );
}
