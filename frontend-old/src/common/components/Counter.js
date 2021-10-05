import React, {useState} from "react";
import Badge from '@mui/material/Badge';
import MailIcon from '@mui/icons-material/Mail';
import { Button } from "@mui/material";
import styled from 'styled-components'
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';
import Stack from '@mui/material/Stack';

export default function Counter(){
    const [count, setCount] = useState(0)

    return (<CounterDiv>
        {count == 0 && <Stack sx={{ width: '200px', margin: '0 auto'}} spacing={2}>
          <Alert severity="warning">
            <AlertTitle>Warning</AlertTitle>
            <strong>메시지가 없습니다.</strong>
          </Alert>
        </Stack>}
        <Badge badgeContent={count >= 0 ? count : setCount(0)} color="secondary">
          <MailIcon color="action" />
        </Badge>
        <br/>
        <Button variant="outlined" onClick={() => setCount(count + 1)}>
            Add
        </Button>
        <SpanStyle/>
        <Button variant="outlined" onClick={() => setCount(count - 1)}>
            Del
        </Button>
        <br/>
    </CounterDiv>)
}

const CounterDiv = styled.div` text-align: center; `
const SpanStyle = styled.span ` margin: 10px; `