import React, { useState, useEffect } from 'react';
import { Container, Typography, TextField, Button, CircularProgress, Grid, Snackbar, Alert, Box } from '@mui/material';
import axios from 'axios';
import WeatherCard from './WeatherCard';
import Popup from './Popup';
import backgroundImage from './weather.jpg';

const API_KEY = '0b63dc946ec6c0bf61fdb5d7031e025b';

const citiesList = [
  'New York', 'London', 'Tokyo', 'Paris', 'Berlin', 'Moscow', 'Sydney', 'Toronto', 'Dubai', 'Singapore', 'Los Angeles', 'Chicago', 'San Francisco', 'Hong Kong', 'Madrid', 'Rome', 'Istanbul', 'Bangkok', 'Seoul', 'Mumbai'
];

const Dashboard = () => {
  const [loading, setLoading] = useState(false);
  const [cities, setCities] = useState([]);
  const [cityName, setCityName] = useState('');
  const [error, setError] = useState(null);
  const [selectedCity, setSelectedCity] = useState(null);
  const [open, setOpen] = useState(false);

  useEffect(() => {
    fetchPredefinedCities();
  }, []);

  const fetchPredefinedCities = async () => {
    setLoading(true);
    setError(null);

    try {
      const promises = citiesList.map(city =>
        axios.get('https://api.openweathermap.org/data/2.5/weather', {
          params: {
            q: city,
            appid: API_KEY,
            units: 'metric'
          }
        })
      );
      const responses = await Promise.all(promises);
      setCities(responses.map(res => res.data));
      setLoading(false);
    } catch (err) {
      console.error('Error fetching cities:', err);
      setError(err);
      setOpen(true);
      setLoading(false);
    }
  };

  const fetchWeather = async () => {
    setLoading(true);
    setError(null);

    try {
      const response = await axios.get(
        'https://api.openweathermap.org/data/2.5/weather',
        {
          params: {
            q: cityName,
            appid: API_KEY,
            units: 'metric',
          },
        }
      );

      setCities([response.data]);
      setLoading(false);
    } catch (err) {
      console.error('Error fetching city:', err);
      setError(err);
      setOpen(true);
      setLoading(false);
    }
  };

  const handleCityChange = (event) => {
    setCityName(event.target.value);
  };

  const handleSearchClick = () => {
    fetchWeather();
  };

  const handleCityClick = (city) => {
    setSelectedCity(city);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleClosePopup = () => {
    setSelectedCity(null);
  };

  return (
    <Box
      sx={{
        backgroundImage: `url(${backgroundImage})`,
        backgroundSize: 'cover',
        minHeight: '100vh',
        padding: '20px',
      }}
    >
      <Container maxWidth="md" style={{ marginTop: '20px' }}>
        <Typography 
        variant="h4" 
        style={{ color: '#fff' }}
        gutterBottom>
          Weather Dashboard
        </Typography>
        <TextField
          label="Enter city name"
          variant="outlined"
          fullWidth
          value={cityName}
          onChange={handleCityChange}
          style={{ marginBottom: '20px', backgroundColor: 'white' }}
        />
        <Button
          variant="contained"
          color="primary"
          onClick={handleSearchClick}
          style={{ marginBottom: '20px' }}
        >
          Search
        </Button>
        {loading && <CircularProgress style={{ marginTop: '20px' }} />}
        <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
          <Alert onClose={handleClose} severity="error" sx={{ width: '100%' }}>
            Error fetching cities. Please try again.
          </Alert>
        </Snackbar>
        <Grid container spacing={2}>
          {cities.map(city => (
            <Grid item xs={12} sm={6} md={4} key={city.id}>
              <WeatherCard
              city={city}
              onCityClick={handleCityClick}
              style={{ cursor: 'pointer' }}
              sx={{
                '&:hover': {
                  transform: 'scale(1.05)',
                  transition: 'transform 0.3s ease-in-out'
                }
              }}
            />
            </Grid>
          ))}
        </Grid>
        {selectedCity && <Popup city={selectedCity} onClose={handleClosePopup} />}
        <Box mt={4}>
          <Button variant="contained" color="secondary" onClick={() => window.location.href = '/'}>
            Return to Home
          </Button>
        </Box>
      </Container>
    </Box>
  );
};

export default Dashboard;
