import React from 'react';
import { Card, CardContent, Typography, Button, Box } from '@mui/material';
import { WiDaySunny, WiRain, WiThunderstorm, WiCloudy, WiSnow } from 'weather-icons-react';

const WeatherCard = ({ city, onCityClick }) => {
  const getWeatherIcon = (weather) => {
    switch (weather) {
      case 'Clear':
        return <WiDaySunny size={64} color="#000" />;
      case 'Rain':
        return <WiRain size={64} color="#000" />;
      case 'Thunderstorm':
        return <WiThunderstorm size={64} color="#000" />;
      case 'Clouds':
        return <WiCloudy size={64} color="#000" />;
      case 'Snow':
        return <WiSnow size={64} color="#000" />;
      default:
        return <WiDaySunny size={64} color="#000" />;
    }
  };

  return (
    <Card onClick={() => onCityClick(city)}>
      <CardContent>
        <Typography variant="h5">{city.name}</Typography>
        <Typography variant="h6">{city.main.temp}°C</Typography>
        <Box>{getWeatherIcon(city.weather[0].main)}</Box>
      </CardContent>
    </Card>
  );
};

export default WeatherCard;
