// src/components/Popup.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Dialog, DialogTitle, DialogContent, Typography, IconButton, Box, CircularProgress, Table, TableContainer, TableHead, TableBody, TableRow, TableCell } from '@mui/material';
import CloseIcon from '@mui/icons-material/Close';
import { WiDaySunny, WiRain, WiThunderstorm, WiCloudy, WiSnow } from 'weather-icons-react';

const API_KEY = '0b63dc946ec6c0bf61fdb5d7031e025b';

const Popup = ({ city, onClose }) => {
  const [forecast, setForecast] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchForecast();
  }, [city]);

  const fetchForecast = async () => {
    setLoading(true);
    try {
      const response = await axios.get('https://api.openweathermap.org/data/2.5/forecast', {
        params: {
          q: city.name,
          appid: API_KEY,
          units: 'metric'
        }
      });
      setForecast(response.data);
      setLoading(false);
    } catch (err) {
      console.error('Error fetching forecast:', err);
      setLoading(false);
    }
  };

  const getWeatherIcon = (weather) => {
    switch (weather) {
      case 'Clear':
        return <WiDaySunny size={32} color="#000" />;
      case 'Rain':
        return <WiRain size={32} color="#000" />;
      case 'Thunderstorm':
        return <WiThunderstorm size={32} color="#000" />;
      case 'Clouds':
        return <WiCloudy size={32} color="#000" />;
      case 'Snow':
        return <WiSnow size={32} color="#000" />;
      default:
        return <WiDaySunny size={32} color="#000" />;
    }
  };

  return (
    <Dialog open onClose={onClose}>
      <DialogTitle>
        {city.name} - 5 Day Forecast
        <IconButton onClick={onClose} style={{ position: 'absolute', right: 8, top: 8 }}>
          <CloseIcon />
        </IconButton>
      </DialogTitle>
      <DialogContent>
        {loading ? (
          <Box display="flex" justifyContent="center" alignItems="center" height="200px">
            <CircularProgress />
          </Box>
        ) : (
          <TableContainer>
            <Table>
              <TableHead>
                <TableRow>
                  <TableCell>Date</TableCell>
                  <TableCell>Weather</TableCell>
                  <TableCell>Temperature (°C)</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {forecast.list.map((item, index) => (
                  <TableRow key={index}>
                    <TableCell>{new Date(item.dt_txt).toLocaleDateString()}</TableCell>
                    <TableCell>
                      <Box display="flex" alignItems="center">
                        {getWeatherIcon(item.weather[0].main)}
                        <Typography variant="body1" style={{ marginLeft: 8 }}>
                          {item.weather[0].main}
                        </Typography>
                      </Box>
                    </TableCell>
                    <TableCell>{item.main.temp}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </DialogContent>
    </Dialog>
  );
};

export default Popup;
