import { createTheme } from '@mui/material/styles';

declare module '@mui/material/styles' {
  interface Palette {
    append: {
      main: string;
      dark: string;
      contrastText: string;
    };
    register: {
      main: string;
      dark: string;
      contrastText: string;
    };
    delete: {
      main: string;
      dark: string;
      contrastText: string;
    };
  }
  interface PaletteOptions {
    append?: {
      main?: string;
      dark?: string;
      contrastText?: string;
    };
    register?: {
      main?: string;
      dark?: string;
      contrastText?: string;
    };
    delete?: {
      main?: string;
      dark?: string;
      contrastText?: string;
    };
    behind?: {
      main?: string;
      dark?: string;
      contrastText?: string;
    };
  }
}

declare module '@mui/material/Button' {
  interface ButtonPropsColorOverrides {
    append: true;
    register: true;
    delete: true;
  }
}

const AppTheme = createTheme({
  typography: {
    fontSize: 12,
    fontFamily: [
      'number',
      'alphabet',
      'BIZ UDゴシック',
      'ヒラギノ角ゴPro W3',
      'Hiragino Kaku Gothic Pro',
      'メイリオ',
      'Meiryo',
      'ＭＳ Ｐゴシック',
      'sans-serif',
    ].join(','),
  },
  components: {
    MuiCssBaseline: {
      styleOverrides: `
        @font-face {
          font-family: 'number';
          src: local('Verdana');
          unicode-range: U+0030-0039;
        }
        @font-face {
          font-family: 'alphabet';
          src: local('Verdana');
          unicode-range: U+0021-007F;
        }
      `,
    },
    MuiToolbar: {
      styleOverrides: {
        root: { minHeight: '34px' },
      },
    },
    MuiFormLabel: {
      styleOverrides: {
        root: { pr: 1 },
        asterisk: { pr: 0, color: '#ff6a61' },
      },
    },
    MuiInputLabel: {
      styleOverrides: {
        root: {
          fontSize: '0.8rem',
          fontWeight: 'bold',
        },
        formControl: {
          transform: 'none',
          transition: 'none',
          alignSelf: 'start',
        },
      },
    },
    MuiOutlinedInput: {
      styleOverrides: {
        root: {
          marginTop: 0,
        },
        input: {
          paddingTop: '8px',
          paddingBottom: '8px',
          height: 'auto',
          backgroundColor: '#fff',
          caretColor: 'auto',
        },
      },
    },
    MuiFormHelperText: {
      styleOverrides: {
        root: {
          marginLeft: 0,
          color: '#d73f2f',
        },
      },
    },
    MuiAutocomplete: {
      styleOverrides: {
        inputRoot: {
          // height: '35px',
          // maxHeight: '35px',
          paddingTop: 0,
          paddingBottom: 0,
          '& .MuiAutocomplete-inputRoot.Mui-disabled': {
            backgroundColor: '#111',
          },
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          maxHeight: '39px',
        },
      },
    },
    // @ts-expect-error - this isn't in the TS because DataGird is not exported from `@mui/material`
    MuiDataGrid: {
      styleOverrides: {
        row: {
          '&:hover': {
            backgroundColor: '#e3eefa !important',
          },
        },
      },
    },
  },
  palette: {
    append: {
      main: '#38bc00',
      dark: '#2c9400',
      contrastText: '#fff',
    },
    register: {
      main: '#303f9f',
      dark: '#283593',
      contrastText: '#fff',
    },
    delete: {
      main: '#424242',
      dark: '#313131',
      contrastText: '#fff',
    },
    behind: {
      main: '#777777',
      dark: '#666666',
      contrastText: '#fff',
    },
  },
});
export default AppTheme;
