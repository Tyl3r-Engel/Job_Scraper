import * as React from 'react';
import './NavBar.css';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import { Grid } from '@mui/material';

export default function ButtonAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static">
        <Toolbar className="navbar">
          <Grid
            justify='flex-end'
            container
            grid-xs-auto
          >
            <Grid item className="navbar-menu">
              <IconButton
                size="large"
                color="inherit"
                aria-label="menu"
              >
                <MenuIcon />
              </IconButton>
            </Grid>

            <Grid item className="navbar-item-container">
                <Typography className="navbar-item" variant="h6" component="div" sx={{ flexGrow: 1 }}>
                  News
                </Typography>
            </Grid>

            <Grid item className="navbar-login">
                <Button className="navbar-item" color="inherit">Login</Button>
            </Grid>
          </Grid>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
