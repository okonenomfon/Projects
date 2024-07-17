import React from 'react';
import { Container, Typography, Box, Button } from '@mui/material';
import { Link } from 'react-router-dom';
import ReactPlayer from 'react-player';
import backgroundVideo from './weather.mp4';

const Home = () => {
  return (
    <Box
      display="flex"
      justifyContent="center"
      alignItems="center"
      height="100vh"
      position="relative"
      overflow="hidden"
    >
      <ReactPlayer
        url={backgroundVideo}
        playing
        loop
        muted
        width="100%"
        height="100%"
        padding="0"
        margin="0"
        style={{ position: 'absolute', top: 0, left: 0, zIndex: -1 }}
      />
      <Container>
        <Typography
          variant="h2"
          component="div"
          style={{ textAlign: 'center', color: '#fff' }}
        >
          Welcome to Eno's Weather App
        </Typography>
        
        <Box display="flex" justifyContent="center" mt={4}>
          <Button
            variant="contained"
            color="primary"
            component={Link}
            to="/dashboard"
          >
            Go to Dashboard
          </Button>
        </Box>

      </Container>
    </Box>
  );
};

export default Home;
