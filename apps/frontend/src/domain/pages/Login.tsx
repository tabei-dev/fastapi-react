// import { ReactElement } from 'react';
import { JSX } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';

import { Container, Paper, Stack, Button } from '@mui/material';
// import { useSetRecoilState } from 'recoil';

import { RHFTextField } from '@/common/components/TextField';
import ValidationError from '@/common/models/validationError';
import { PAGE_LINKS } from '@/domain/config/consts';
import authService from '@/domain/services/authService';

/**
 * ログインページ
 * @returns {JSX.Element} JSX.Element
 */
const Login = (): JSX.Element => {
  const { control, handleSubmit, setError } = useForm({
    mode: 'onBlur',
    reValidateMode: 'onChange',
    defaultValues: {
      username: '',
      password: '',
    },
  });

  const navigate = useNavigate();

  // const setAuth = useSetRecoilState(authState);

  /**
   * ログインボタンクリックイベントハンドラ
   * @param user ユーザー情報
   */
  const handleLoginClick = async (user: { username: string; password: string }) => {
    try {
      await authService.login(user);
      // setAuth(auth); // 認証情報をRecoilに保存
    } catch (error) {
      if (error instanceof ValidationError) {
        setError(error.fieldname as 'username' | 'password', { message: error.message });
      }
      return;
    }

    navigate(PAGE_LINKS.MENU);
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
export default Login;
