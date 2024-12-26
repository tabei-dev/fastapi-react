import { JSX } from 'react';
import { useForm } from 'react-hook-form';

import { Container, Paper, Stack, Button } from '@mui/material';

import { login } from '@/controllers/authController';
import { RHFTextField } from '@/parts/TextField';

/**
 * ログインページ
 * @returns {JSX.Element} JSX.Element
 */
const LoginPage = (): JSX.Element => {
  const { control, handleSubmit } = useForm({
    mode: 'onBlur',
    reValidateMode: 'onChange',
    defaultValues: {
      username: '',
      password: '',
    },
  });

  /**
   * ログインボタンクリックイベントハンドラ
   * @param user ユーザー情報
   */
  const handleLoginClick = async (user: { username: string; password: string }) => {
    try {
      await login(user);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  return (
    <Container maxWidth="sm" sx={{ pt: 10 }}>
      <Paper sx={{ overflow: 'visible' }} elevation={3}>
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
