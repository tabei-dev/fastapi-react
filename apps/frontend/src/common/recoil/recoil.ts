import { atom } from 'recoil';

import { EMPTY, Empty } from '@/common/config/consts';
import Auth from '@/domain/models/auth';

/**
 * 認証情報
 */
export const authState = atom({
  key: 'authState',
  default: EMPTY as Auth | Empty,
});

/**
 * 選択中のカテゴリとページ
 */
export const selectedCategoryAndPageState = atom({
  key: 'selectedCategoryAndPageState',
  default: { category: '', page: '' } as { category: string; page: string },
});
