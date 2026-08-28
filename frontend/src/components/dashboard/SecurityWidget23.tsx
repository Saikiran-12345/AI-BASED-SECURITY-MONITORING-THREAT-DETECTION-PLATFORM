import React from 'react';
import { Card, CardContent, Typography, Box } from '@mui/material';

interface SecurityWidget23Props {
    data?: any;
    title?: string;
}

export default function SecurityWidget23({ data, title = 'SecurityWidget23' }: SecurityWidget23Props) {
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
