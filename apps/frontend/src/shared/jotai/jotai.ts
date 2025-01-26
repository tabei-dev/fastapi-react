// import { atom } from 'recoil';
import { atom } from 'jotai';

import Auth from '@/domain/models/auth';
import { EMPTY, Empty } from '@/shared/config/consts';

/**
 * 認証情報
 */
// export const authState = atom({
//   key: 'authState',
//   default: EMPTY as Auth | Empty,
// });
export const authState = atom(EMPTY as Auth | Empty);

/**
 * 選択中のカテゴリとページ
 */
// export const selectedCategoryAndPageState = atom({
//   key: 'selectedCategoryAndPageState',
//   default: { category: '', page: '' } as { category: string; page: string },
// });
export const selectedCategoryAndPageState = atom({ category: '', page: '' } as {
  category: string;
  page: string;
});
