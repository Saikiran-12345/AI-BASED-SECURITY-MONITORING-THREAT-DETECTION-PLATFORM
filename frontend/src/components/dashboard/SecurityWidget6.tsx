import React from 'react';
import { Card, CardContent, Typography, Box } from '@mui/material';

interface SecurityWidget6Props {
    data?: any;
    title?: string;
}

export default function SecurityWidget6({ data, title = 'SecurityWidget6' }: SecurityWidget6Props) {
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
