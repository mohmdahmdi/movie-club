import { useState } from "react";
import axios, { AxiosRequestConfig, AxiosResponse, AxiosError } from "axios";

const useAxios = <T>() => {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<AxiosError | null>(null);
  const [loading, setLoading] = useState(false);

  const makeRequest = async (config: AxiosRequestConfig): Promise<T> => {
    setLoading(true);
    setError(null);

    try {
      const response: AxiosResponse<T> = await axios(config);
      setData(response.data);
      return response.data;
    } catch (err) {
      const axiosError = err as AxiosError;
      setError(axiosError);
      throw axiosError;
    } finally {
      setLoading(false);
    }
  };

  const get = (url: string, config: AxiosRequestConfig = {}): Promise<T> =>
    makeRequest({ ...config, method: "GET", url });

  const post = (
    url: string,
    data: unknown,
    config: AxiosRequestConfig = {}
  ): Promise<T> => makeRequest({ ...config, method: "POST", url, data });

  const put = (
    url: string,
    data: unknown,
    config: AxiosRequestConfig = {}
  ): Promise<T> => makeRequest({ ...config, method: "PUT", url, data });

  const del = (url: string, config: AxiosRequestConfig = {}): Promise<T> =>
    makeRequest({ ...config, method: "DELETE", url });

  return { data, error, loading, get, post, put, del };
};

export default useAxios;
