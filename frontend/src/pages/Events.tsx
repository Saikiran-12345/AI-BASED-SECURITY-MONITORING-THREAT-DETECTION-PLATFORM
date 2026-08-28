import React, { useEffect, useState } from 'react';
import { Box, Typography, Paper, Table, TableBody, TableCell, TableContainer, TableHead, TableRow, TablePagination, Chip } from '@mui/material';
import api from '../services/api';
import type { SecurityEvent } from '../types';
import { format } from 'date-fns';

export default function Events() {
  const [events, setEvents] = useState<SecurityEvent[]>([]);
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    fetchEvents();
  }, [page, rowsPerPage]);

  const fetchEvents = async () => {
    try {
      const res = await api.get(`/events/?page=${page + 1}&size=${rowsPerPage}`);
      setEvents(res.data.results);
      setTotal(res.data.count);
    } catch (err) {
      console.error(err);
    }
  };

  const handleChangePage = (event: unknown, newPage: number) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
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
      <Typography variant="h4" gutterBottom>Security Events</Typography>
      <Paper sx={{ width: '100%', overflow: 'hidden' }}>
        <TableContainer sx={{ maxHeight: 600 }}>
          <Table stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell>Timestamp</TableCell>
                <TableCell>Event Type</TableCell>
                <TableCell>User</TableCell>
                <TableCell>Severity</TableCell>
                <TableCell>Risk Score</TableCell>
                <TableCell>Source</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {events.map((row) => (
                <TableRow hover key={row.id}>
                  <TableCell>{format(new Date(row.timestamp), 'yyyy-MM-dd HH:mm:ss')}</TableCell>
                  <TableCell>{row.event_type}</TableCell>
                  <TableCell>{row.user_name || 'System'}</TableCell>
                  <TableCell>
                    <Chip label={row.severity} color={getSeverityColor(row.severity) as any} size="small" />
                  </TableCell>
                  <TableCell>{row.risk_score}</TableCell>
                  <TableCell>{row.source}</TableCell>
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
          onPageChange={handleChangePage}
          onRowsPerPageChange={handleChangeRowsPerPage}
        />
      </Paper>
    </Box>
  );
}
