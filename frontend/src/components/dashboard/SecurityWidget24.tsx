import React from 'react';
import { Card, CardContent, Typography, Box } from '@mui/material';

interface SecurityWidget24Props {
    data?: any;
    title?: string;
}

export default function SecurityWidget24({ data, title = 'SecurityWidget24' }: SecurityWidget24Props) {
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
