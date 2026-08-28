import React from 'react';
import { Card, CardContent, Typography, Box } from '@mui/material';

interface RecentAlertsListProps {
    data?: any;
    title?: string;
}

export default function RecentAlertsList({ data, title = 'RecentAlertsList' }: RecentAlertsListProps) {
    return (
        <Card sx={{ height: '100%' }}>
            <CardContent>
                <Typography variant="h6" color="textSecondary" gutterBottom>
                    {title}
                </Typography>
                <Box sx={{ mt: 2, display: 'flex', justifyContent: 'center', alignItems: 'center', height: 200 }}>
                    <Typography variant="body2" color="textSecondary">
                        Data visualization for {title} will be rendered here.
                    </Typography>
                </Box>
            </CardContent>
        </Card>
    );
}
