import { useForm } from 'react-hook-form';

import { Container, Paper, Box, Stack, InputLabel, Button } from '@mui/material';

import { login } from '@/controllers/loginController';
import { RHFTextField } from '@/parts/TextField';

const LoginPage = () => {
  const { control, handleSubmit, getValues } = useForm({
    mode: 'onBlur',
    reValidateMode: 'onChange',
    defaultValues: {
      username: '',
      password: '',
    },
  });

  const handleLoginClick = async (data: { username: string; password: string }) => {
    try {
      const response = await login(data);
      console.log('Login successful:', response);
      // トークンを保存するなどの処理を追加
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <Container maxWidth="sm" sx={{ pt: 10 }}>
      {/* <h1>Login</h1> */}
      <Paper sx={{ overflow: 'visible' }} elevation={3}>
        {/* センタリング */}
        <Stack sx={{ width: '90%', margin: '0 auto', py: 4 }} spacing={2}>
          {/* <InputLabel htmlFor="username">ユーザー名</InputLabel> */}
          <RHFTextField
            sx={{ width: '100%' }}
            label="ユーザー名"
            controller={{ control, name: 'username', rules: { required: '必須入力項目です' } }}
          />
          {/* <InputLabel htmlFor="password">パスワード</InputLabel> */}
          <RHFTextField
            sx={{ width: '100%' }}
            label="パスワード"
            controller={{ control, name: 'password', rules: { required: '必須入力項目です' } }}
            passwordType
          />
          <Button
            color="primary"
            variant="contained"
            size="large"
            sx={{ width: '100%', mt: 2 }}
            onClick={handleSubmit(handleLoginClick)}
            style={{ marginTop: '50px' }}
          >
            ログイン
          </Button>
        </Stack>
      </Paper>
    </Container>
  );
};
export default LoginPage;
