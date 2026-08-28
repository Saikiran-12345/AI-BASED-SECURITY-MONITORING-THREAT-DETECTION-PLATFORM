import React from 'react';
import { Card, CardContent, Typography, Box, Grid } from '@mui/material';

interface AdvancedWidget21Props {
    data?: any;
    title?: string;
    refreshInterval?: number;
}

export default function AdvancedWidget21({ data, title = 'Advanced Security Metric 21', refreshInterval = 3000 }: AdvancedWidget21Props) {
    // Complex metric calculation representation
    const metrics = [
        { label: 'Threat Score', value: 21 * 2 },
        { label: 'Confidence', value: '21%' },
        { label: 'Impact Level', value: 21 % 3 === 0 ? 'CRITICAL' : 'HIGH' }
    ];

    return (
        <Card sx={{ height: '100%', minHeight: 250, boxShadow: 3 }}>
            <CardContent>
                <Typography variant="h6" color="primary" gutterBottom>
                    {title}
                </Typography>
                <Box sx={{ mt: 2 }}>
                    <Grid container spacing={2}>
                        {metrics.map((m, idx) => (
                            <Grid item xs={4} key={idx}>
                                <Box textAlign="center" p={1} bgcolor="background.default" borderRadius={1}>
                                    <Typography variant="caption" color="textSecondary">{m.label}</Typography>
                                    <Typography variant="h5">{m.value}</Typography>
                                </Box>
                            </Grid>
                        ))}
                    </Grid>
                </Box>
                <Box sx={{ mt: 3, p: 2, bgcolor: 'action.hover', borderRadius: 1 }}>
                    <Typography variant="body2">
                        Real-time analytics engine 21 is actively monitoring incoming packet streams and application logs.
                        Current refresh interval is set to {refreshInterval}ms.
                    </Typography>
                </Box>
            </CardContent>
        </Card>
    );
}
