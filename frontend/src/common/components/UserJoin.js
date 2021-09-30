import React, {useState} from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';

import { useDispatch } from 'react-redux'
import { addUserAction } from 'reducers/user.reducer'
import { userRegister } from 'api';

function Copyright(props) {
  return (
    <Typography variant="body2" color="text.secondary" align="center" {...props}>
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const theme = createTheme();

export default function UserJoin() {
  const [user, setUser] = useState({
    username: '',
    pwd: '',
    email: '',
    birth: '',
    address: ''
  })
  const {username, pwd, email, birth, address} = user
  // const dispatch = useDispatch()
  const handleSubmit = e => {
    e.preventDefault();
    alert(`가입 회원정보: ${JSON.stringify(user)}`)
    userRegister({user})
    .then(res => {alert(`회원가입 완료: ${res.data.result}`)})
    .catch(err => {alert(`회원가입 실패: ${err}`)})
    // addUser(user)
  };
  // const addUser = payload => (dispatch(addUserAction(payload)))
  const handleChange = e => {
      e.preventDefault()
      const {name, value} = e.target
      setUser({
        ...user,
        [name]: value
      })
  }
  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="xs">
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOutlinedIcon />
          </Avatar>
          <Typography component="h1" variant="h5">
            Sign in
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }} method="POST">
          <TextField
              margin="normal"
              required
              fullWidth
              id="username"
              label="username"
              name="username"
              value = {username}
              onChange = {handleChange}
              autoComplete="username"
              autoFocus
            />

            <TextField
              margin="normal"
              required
              fullWidth
              name="pwd"
              label="Password"
              type="password"
              id="password"
              value = {pwd}
              onChange = {handleChange}
              autoComplete="current-password"
            />


            <TextField
              margin="normal"
              required
              fullWidth
              id="email"
              label="Email Address"
              name="email"
              value = {email}
              onChange = {handleChange}
              autoComplete="email"
              autoFocus
            />

            <TextField
              margin="normal"
              required
              fullWidth
              id="birth"
              label="birth"
              name="birth"
              value = {birth}
              onChange = {handleChange}
              autoComplete="birth"
              autoFocus
            />

            <TextField
              margin="normal"
              required
              fullWidth
              id="address"
              label="Address"
              name="address"
              value = {address}
              onChange = {handleChange}
              autoComplete="address"
              autoFocus
            />
            <FormControlLabel
              control={<Checkbox value="remember" color="primary" />}
              label="Remember me"
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Sign In
            </Button>
          </Box>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}